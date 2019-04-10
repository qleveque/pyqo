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

Env_UserRemoveDuplicates(name, value := "", location := ""){
   RegRead, registry, % (location == "") ? "HKEY_CURRENT_USER\Environment" : location, % name
   Sort, registry, U D`;
   type := (type) ? type : (registry ~= "%") ? "REG_EXPAND_SZ" : "REG_SZ"
   RegWrite, % type , % (location == "") ? "HKEY_CURRENT_USER\Environment" : location, % name, % registry
   return (ErrorLevel) ? -1 : 0
}

Env_SystemRemoveDuplicates(name, value := ""){
   return (A_IsAdmin) ? Env_UserRemoveDuplicates(name, value, "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment") : -3
}

ExpandEnvironmentStrings(ByRef vInputString)
{
   ; get the required size for the expanded string
   vSizeNeeded := DllCall("ExpandEnvironmentStrings", "Str", vInputString, "Int", 0, "Int", 0)
   If (vSizeNeeded == "" || vSizeNeeded <= 0)
      return False ; unable to get the size for the expanded string for some reason

   vByteSize := vSizeNeeded + 1
   If (A_IsUnicode) { ; Only 64-Bit builds of AHK_L will return 8, all others will be 4 or blank
      vByteSize *= 2 ; need to expand to wide character sizes
   }
   VarSetCapacity(vTempValue, vByteSize, 0)

   ; attempt to expand the environment string
   If (!DllCall("ExpandEnvironmentStrings", "Str", vInputString, "Str", vTempValue, "Int", vSizeNeeded))
      return False ; unable to expand the environment string
   vInputString := vTempValue

   ; return success
   Return True
}