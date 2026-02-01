# STEPExportOptions.wantTempIds Property

Parent Object: [STEPExportOptions](STEPExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/STEPExportOptions.h>

## Description

Indicates if the STEP file should include the Fusion temporary IDs for faces and edges. Outside services can use these IDs with the findByTempId method of the BRepBody, which will return the given entity. The default is false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sTEPExportOptions\_var" is a variable referencing a STEPExportOptions object. |

"sTEPExportOptions\_var" is a variable referencing a STEPExportOptions object. ```` ``` #include <Fusion/Fusion/STEPExportOptions.h>  // Get the value of the property. boolean propertyValue = sTEPExportOptions_var->wantTempIds();  // Set the value of the property, where value_var is a boolean. bool returnValue = sTEPExportOptions_var->wantTempIds(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |