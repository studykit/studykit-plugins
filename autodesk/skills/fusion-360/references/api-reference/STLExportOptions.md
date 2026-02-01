# STLExportOptions Object

Derived from: [ExportOptions](ExportOptions.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/STLExportOptions.h>

## Description

Defines that a STL export is to be done and specifies the various options.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](STLExportOptions_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [aspectRatio](STLExportOptions_aspectRatio.htm) | Gets and sets the minimum aspect ratio for that triangles that are generated for the mesh. Setting this property will automatically set the meshRefinement to MeshRefinementCustom. The default is the value associated with medium mesh refinement. |
| [availablePrintUtilities](STLExportOptions_availablePrintUtilities.htm) | Returns a list of the known available print utilities. These strings can be used to set the PrintUtility property to specify which print utility to open the STL file in. |
| [filename](STLExportOptions_filename.htm) | Gets and sets the filename that the exported file will be written to. This can be empty in the case of STL export and sending the result to the mesh editor. |
| [geometry](STLExportOptions_geometry.htm) | Specifies the geometry to export. This can be an Occurrence, or the root Component. For STL, OBJ, and 3MF export, it can be a BRepBody. For DXF export, it can be a sketch of flat pattern. |
| [isBinaryFormat](STLExportOptions_isBinaryFormat.htm) | Indicates if the STL file is to be an ASCII or binary STL format. The default is true. |
| [isOneFilePerBody](STLExportOptions_isOneFilePerBody.htm) | If the input is an Occurrence or the root Component, this specifies if a single file should be created containing all of the bodies within that occurrence or component or if multiple files should be created; one for each body. If multiple files are created, the body name is appended to the filename. The default is false. |
| [isValid](STLExportOptions_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [maximumEdgeLength](STLExportOptions_maximumEdgeLength.htm) | Gets and sets the maximum length of any mesh edge. This is defined in centimeter. Setting this property will automatically set the meshRefinement to MeshRefinementCustom. The default is the value associated with medium mesh refinement. |
| [meshRefinement](STLExportOptions_meshRefinement.htm) | Gets and sets the current simple mesh refinement settings. Setting this property will reset the surfaceDeviation, normalDeviation, maximumEdgeLength, and aspectRatio to values that correspond to the specified mesh refinement. The default is MeshRefinementMedium. |
| [normalDeviation](STLExportOptions_normalDeviation.htm) | Gets and sets the current normal deviation, or the angle the mesh normals at the vertices can deviate from the actual surface normals. This is defined in radians. Setting this property will automatically set the meshRefinement to MeshRefinementCustom. The default is the value associated with medium mesh refinement. |
| [objectType](STLExportOptions_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [printUtility](STLExportOptions_printUtility.htm) | Specifies which print utility to use when opening the STL file if the sendToPrintUtility property is true. The value of this property can be one of the strings returned by the availalbePrintUtilities property, which will specify one of the know print utilities. You can also specify a custom print utility by specifying the full path to the print utility executable. The default value of this property is the last setting specified in the user-interface. |
| [sendToPrintUtility](STLExportOptions_sendToPrintUtility.htm) | Gets and sets whether the created STL file will be sent to the print utility specified by the printUtility property. If this is false a filename must be defined. |
| [surfaceDeviation](STLExportOptions_surfaceDeviation.htm) | Gets and sets the current surface deviation, or the distance the mesh can deviate from the actual surface. This is defined in centimeter. Setting this property will automatically set the meshRefinement to MeshRefinementCustom. The default is the value associated with medium mesh refinement. |
| [unitType](STLExportOptions_unitType.htm) | Gets and sets the units to use for the created STL file. When the STLExportOptions object is created, this property is initialized with the default units specified for the Design. |

## Accessed From

[ExportManager.createSTLExportOptions](ExportManager_createSTLExportOptions.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Export to other formats API Sample](ExportToOtherFormats_Sample.htm) | Demonstrates exporting the active design to IGES, STEP, SAT, SMT, F3D and STL formats. To run this sample, have a design open and run the script. It will write out the translated files to a temp directory, which will it show in a message box. |
| [STLExport API Sample](STLExport_Sample.htm) | Demonstrates how to export f3d to STL format. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |