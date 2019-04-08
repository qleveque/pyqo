obj := ComObjCreate("QTTabBarLib.Scripting")

dir = %1%
n_args = %0%

dir := RegExReplace(dir, "/", "\")

if(n_args>1)
{
    obj.OpenWindow(dir)
}
else
{
    obj.Open(dir)
}