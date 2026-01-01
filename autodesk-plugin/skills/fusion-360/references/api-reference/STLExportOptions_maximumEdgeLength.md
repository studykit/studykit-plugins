# STLExportOptions.maximumEdgeLength Property

Parent Object: [STLExportOptions](STLExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/STLExportOptions.h>

## Description

Gets and sets the maximum length of any mesh edge. This is defined in centimeter. Setting this property will automatically set the meshRefinement to MeshRefinementCustom. The default is the value associated with medium mesh refinement.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sTLExportOptions\_var" is a variable referencing a STLExportOptions object. |

"sTLExportOptions\_var" is a variable referencing a STLExportOptions object. ```` ``` #include <Fusion/Fusion/STLExportOptions.h>  // Get the value of the property. double propertyValue = sTLExportOptions_var->maximumEdgeLength();  // Set the value of the property, where value_var is a double. bool returnValue = sTLExportOptions_var->maximumEdgeLength(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |