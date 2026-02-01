# STEPImportOptions.isViewFit Property

Parent Object: [STEPImportOptions](STEPImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/STEPImportOptions.h>

## Description

Specifies if the camera should be adjusted to fit the geometry of the import. This defaults to true, which will cause a change in the current view. Setting this to false will leave the view as-is and just import the geometry.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sTEPImportOptions\_var" is a variable referencing a STEPImportOptions object. |

"sTEPImportOptions\_var" is a variable referencing a STEPImportOptions object. ```` ``` #include <Core/Application/STEPImportOptions.h>  // Get the value of the property. boolean propertyValue = sTEPImportOptions_var->isViewFit();  // Set the value of the property, where value_var is a boolean. bool returnValue = sTEPImportOptions_var->isViewFit(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |