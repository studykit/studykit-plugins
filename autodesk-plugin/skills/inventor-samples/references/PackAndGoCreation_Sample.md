# Pack and go

## Description

This sample demonstrates using pack and go interop to create a package.

## Code Samples

* [VB.Net](#VB.Net)
* [C#](#C#)
* [C++](#C++)

Create a VB.Net project and add the reference to the pack and go type interop binary Autodesk.PackAndGo.Interop.dll which is in the Bin folder of Inventor installation folder.

```
Public Sub PackAndGoSample()
    Dim oPacknGoComp As New PackAndGoLib.PackAndGoComponent

    Dim oPacknGo As PackAndGoLib.PackAndGo
    oPacknGo = oPacknGoComp.CreatePackAndGo("C:\Temp\Source\Assembly1.iam", "C:\Temp\Destination")

    ' Set the design project. This defaults to the current active project.
    oPacknGo.ProjectFile = "C:\Temp\Source\Test.ipj"

    Dim sRefFiles = New String() {}
    Dim sMissFiles = New Object

    ' Set the options
    oPacknGo.IsSkippingLibraries = True
    oPacknGo.IsSkippingStyles = True
    oPacknGo.IsSkippingTemplates = True
    oPacknGo.IsCollectingWorkgroups = False
    oPacknGo.IsKeepingFolderHierarchy = True
    oPacknGo.IncludeLinkedFiles = True

    ' Get the referenced files
    oPacknGo.SearchForReferencedFiles(sRefFiles, sMissFiles)

    ' Add the referenced files for package
    oPacknGo.AddFilesToPackage (sRefFiles)

    ' Start the pack and go to create the package
    oPacknGo.CreatePackage()
End Sub
```

Create a C#.Net project and add the reference to the pack and go type interop binary Autodesk.PackAndGo.Interop.dll which is in the Bin folder of Inventor installation folder.

```
public void PackAndGoSample()
{
    PackAndGoComponent packAndGoComp = new PackAndGoComponent();
    PackAndGo packAndGo=packAndGoComp.CreatePackAndGo("C:\\Temp\\Source\\Assembly1.iam","C:\\Temp\\Destination");

    // Set the design project. This defaults to the current active project.
    packAndGo.ProjectFile = "C:\\Temp\\Source\\Test.ipj";

    string[] refFiles = new string[]{};
    object refMissFiles = new object();

    // Set the options
    packAndGo.IsSkippingLibraries = true;
    packAndGo.IsSkippingStyles = true;
    packAndGo.IsSkippingTemplates = true;
    packAndGo.IsCollectingWorkgroups = false;
    packAndGo.IsKeepingFolderHierarchy = true;
    packAndGo.IncludeLinkedFiles = true;

    // Get the referenced files
    packAndGo.SearchForReferencedFiles(out refFiles,out refMissFiles);

    // Add the referenced files for package
    packAndGo.AddFilesToPackage(refFiles);

    // Start the pack and go to create the package
    packAndGo.CreatePackage();
}
```

Create a C++ project and add the include the Bin folder of Inventor installation folder where the DTPackAndGo.tlb is located.

```
#import "DTPackAndGo.tlb" no_namespace named_guids \
     raw_dispinterfaces raw_method_prefix("") \
     high_method_prefix("Method")

void PackAndGoSample()
{
  HRESULT Result = NOERROR;

  CComPtr<IPackAndGoComponent> packAndGoComp;
  Result = packAndGoComp.CoCreateInstance(CLSID_PackAndGoComponent);

  CComPtr<IPackAndGo> packAndGo =
    packAndGoComp->MethodCreatePackAndGo(
      L"C:\\Temp\\Source\\Assembly1.iam", L"C:\\Temp\\Destination");

  // Set the design project. This defaults to the
  // current active project.
  packAndGo->ProjectFile = L"C:\\Temp\\Source\\Test.ipj";

  // Set the options
  packAndGo->SkipLibraries = true;
  packAndGo->SkipStyles = true;
  packAndGo->SkipTemplates = true;
  packAndGo->CollectWorkgroups = false;
  packAndGo->KeepFolderHierarchy = true;
  packAndGo->IncludeLinkedFiles = true;

  SAFEARRAY * refFiles = NULL;
  VARIANT refMissFiles;

  // Get the referenced files
  packAndGo->MethodSearchForReferencedFiles(
    &refFiles, &refMissFiles);

  // Add the referenced files for package
  packAndGo->MethodAddFilesToPackage(&refFiles);

  // Start the pack and go to create the package
  // OverrideExistingFiles = TRUE
  packAndGo->MethodCreatePackage(VARIANT_TRUE);
}
```
