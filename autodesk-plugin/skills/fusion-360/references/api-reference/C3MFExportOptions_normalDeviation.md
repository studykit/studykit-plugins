# C3MFExportOptions.normalDeviation Property

Parent Object: [C3MFExportOptions](C3MFExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/C3MFExportOptions.h>

## Description

Gets and sets the current normal deviation, or the angle the mesh normals at the vertices can deviate from the actual surface normals. This is defined in radians. Setting this property will automatically set the meshRefinement to MeshRefinementCustom. The default is the value associated with medium mesh refinement.

## Syntax

* [Python](#Python)
* [C++](#C++)

"c3MFExportOptions\_var" is a variable referencing a C3MFExportOptions object. |

"c3MFExportOptions\_var" is a variable referencing a C3MFExportOptions object. ```` ``` #include <Fusion/Fusion/C3MFExportOptions.h>  // Get the value of the property. double propertyValue = c3MFExportOptions_var->normalDeviation();  // Set the value of the property, where value_var is a double. bool returnValue = c3MFExportOptions_var->normalDeviation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |