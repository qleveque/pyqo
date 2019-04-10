Env_UserAdd(name, value, type := "", location := ""){
   RegRead, registry, % (location == "") ? "HKEY_CURRENT_USER\Environment" : location, % name
   if (!ErrorLevel) {
      Loop, parse, registry, `;
      {
         if (A_LoopField == value)
            return -2
      }
      registry .= (registry ~= "(;$|^$)") ? "" : ";"
      value := registry . value
   }
   type := (type) ? type : (value ~= "%") ? "REG_EXPAND_SZ" : "REG_SZ"
   RegWrite, % type , % (location == "") ? "HKEY_CURRENT_USER\Environment" : location, % name, % value
   SendMessage, 0x1A,0,"Environment",, ahk_id 0xFFFF ; 0x1A is WM_SETTINGCHANGE
   RefreshEnvironment()
   return (ErrorLevel) ? -1 : 0
}

Env_SystemAdd(name, value, type := ""){
   return (A_IsAdmin) ? Env_UserAdd(name, value, type, "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment") : -3
}

Env_UserSub(name, value, type := "", location := ""){
   RegRead, registry, % (location == "") ? "HKEY_CURRENT_USER\Environment" : location, % name
   if ErrorLevel
      return -2

   Loop, parse, registry, `;
   {
      if (A_LoopField != value) {
         output .= (A_Index > 1 && output != "") ? ";" : ""
         output .= A_LoopField
      }
   }

   if (output != "") {
      type := (type) ? type : (output ~= "%") ? "REG_EXPAND_SZ" : "REG_SZ"
      RegWrite, % type , % (location == "") ? "HKEY_CURRENT_USER\Environment" : location, % name, % output
   }
   else
      RegDelete, % (location == "") ? "HKEY_CURRENT_USER\Environment" : location, % name
   SendMessage, 0x1A,0,"Environment",, ahk_id 0xFFFF ; 0x1A is WM_SETTINGCHANGE
   RefreshEnvironment()
   return (ErrorLevel) ? -1 : 0
}

Env_SystemSub(name, value, type := ""){
   return (A_IsAdmin) ? Env_UserSub(name, value, type, "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment") : -3
}

RefreshEnvironment()
{
   Path := ""
   PathExt := ""
   RegKeys := "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment,HKCU\Environment"
   Loop, Parse, RegKeys, CSV
   {
      Loop, Reg, %A_LoopField%, V
      {
         RegRead, Value
         If (A_LoopRegType == "REG_EXPAND_SZ" && !ExpandEnvironmentStrings(Value))
            Continue
         If (A_LoopRegName = "PATH")
            Path .= Value . ";"
         Else If (A_LoopRegName = "PATHEXT")
            PathExt .= Value . ";"
         Else
            EnvSet, %A_LoopRegName%, %Value%
      }
   }
   EnvSet, PATH, %Path%
   EnvSet, PATHEXT, %PathExt%
}
