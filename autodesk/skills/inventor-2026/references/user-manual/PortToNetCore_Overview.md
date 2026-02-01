# Port .Net Framework-based project to .Net

Inventor 2025  has migrated from .Net Framework to .Net 8, it is
recommended to port the .Net Framework-based projects to .Net 8 to keep
compatibility. This article demonstrates how to port Inventor VB.net/C# projects
from .Net Framework-based to .Net 8-based, and also C++/CLI settings for C++ projects which use managed code.

## Environment Preparation:

1. **Visual Studio:**Install Visual Studio 17.8 or later version which supports targeting .Net 8.0
   SDK, refer to the [Version
   requirements for .NET 8 SDK](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/8.0/version-requirements).
2. **.Net 8.0 SDK:**Install .Net 8.0 SDK, refer to the [Download .NET SDKs for Visual Studio](https://dotnet.microsoft.com/en-us/download/visual-studio-sdks).
3. **.NET
   Upgrade Assistant:**Install the Visual Studio extension “.NET Upgrade Assistant”, refer to [Install the .NET Upgrade Assistant](https://learn.microsoft.com/en-us/dotnet/core/porting/upgrade-assistant-install):

   ![](../images/NETUpgradeAssistant.png)

## Port to .Net 8 process (C# and VB.net projects)

1. **Open an Inventor project (below is based on a simple VB.net Inventor addin as
   example, which is targeted to .Net Framework 4.8).**

   ![](../images/NetFrameworkProperties.png)
2. **Right click the project, and choose Upgrade command:**

   ![](../images/UpgradeNetStep1.png)
3. **Choose “Upgrade project to a newer .NET version”:**

   ![](../images/UpgradeNetStep2.png)
4. **Choose
   “In-place project upgrade”, and click Next:**

   ![](../images/UpgradeNetStep3.png)
5. **Choose “.NET 8.0” and click Next:**

   ![](../images/UpgradeNetStep4.png)
6. **Select all if you are not sure which ones need to migrate and click Upgrade selection:**

   ![](../images/UpgradeNetStep5.png)
7. **Now the migration result is as below:**

   ![](../images/UpgradeNetStep6.png)
8. **Check the Project Properties the Target framework is .NET 8.0 now:**

   ![](../images/UpgradeNetStep7.png)
9. **Re-reference Autodesk.Inventor.interop.dll from C:\Program Files\Autodesk\Inventor 2025\Bin\ folder, and set the “Embed Interop Types” to False, “Copy Local” to True:**

   ![](../images/UpgradeNetStep8.png)
10. **Edit the InventorAddinSample.vbproj using a text editor, and delete the below <PostBuildEvent> tag for Post Build Event:**

    ![](../images/UpgradeNetStep9.png)
11. **Add below <PropertyGroup> tag to <Project> for embedding manifest file to the result binary:**

    ``` <PropertyGroup>   <ApplicationManifest>$projectname$.X.manifest</ApplicationManifest> </PropertyGroup> ``` |

    ![](../images/UpgradeNetStep10.png)
12. **Recompile the project:**

    ![](../images/UpgradeNetStep11.png)

13. **Deploy your addin to proper locations:**

    Place the Autodesk.InventorAddinSample.Inventor.addin to C:\Program Files\Autodesk\Inventor 2025\Bin\Addins\ folder.

    Place the binary \InventorAddinSample\bin\Debug\net8.0-windows7.0\InventorAddinSample.dll to C:\Program Files\Autodesk\Inventor 2025\Bin\ folder.
14. **Launch Inventor and check if the addin now can be loaded successfully.**

## Port to .Net 8 process (C++/CLI properties in C++ projects)

*This is for a C++ project has C++/CLI properties set for managed code. As the “.NET Upgrade Assistant” tool doesn’t work for C++/CLI upgrade in C++ projects, below steps demonstrate how to upgrade the C++/CLI properties manually.*

1. **Open project in Visual Studio, right click the project and choose Properties command.**- **Navigate to Advanced:**

     ![](../images/UpgradeCLIStep1.png)

   - **Change the Common Language Runtime Support to  .NET Core Runtime Support (/clr:netcore) from the dropdown list, then click Apply button:**

     ![](../images/UpgradeCLIStep2.png)

   - **Change the .Net Core Target Framework to  .NET 8.0 from the dropdown list, and click OK button:**

     ![](../images/UpgradeCLIStep3.png)

   - **Open the project file using text editor, delete the system references:**

     ![](../images/UpgradeCLIStep4.png)

   - **Add framework references to WPF/WinForm is necessary, such as:**

     ``` <!-- Reference all of WPF --> <FrameworkReference Include="Microsoft.WindowsDesktop.App.WPF" /> ``` |
   - **Search if there are individual files have the “CompileAsManaged” property. Remove it as this property will cause build error and the files are compiled as managed by default:**

     ``` <CompileAsManaged Condition="'$(Configuration)|$(Platform)'=='Debug|x64'">true</CompileAsManaged> ``` |
   - **Navigate to project properties page, and go to C/C++->General, and choose No Common Language Runtime Support for Common Language Runtime:**

     ![](../images/UpgradeCLIStep5.png)

   - **Navigate to Precompiled Headers, choose Not Using Precompiled Headers for Precompiled Header:**

     ![](../images/UpgradeCLIStep6.png)

   - **Reference Autodesk.Inventor.interop.dll from C:\Program Files\Autodesk\Inventor 2025\Bin\.**

   - **Rebuild project and deploy the binaries and check if everything works.**

## More infomation:

More infomation can be found from Autodesk Beta Forum page :[.Net Framework based Inventor projects upgrade to .Net 8 - (Inventor 2025)](https://feedback.autodesk.com/project/forum/thread.html?cap=fb14413735ee42c99624e3793b19a0b2&forid=%7Bdeb2224c-a845-44a8-a857-a54f58c97618%7D&topid=%257B5677A04A-F17E-4EAE-B1BF-8983ADD137E5%257D&j=5677a04af17e4eaeb1bf8983add137e5)