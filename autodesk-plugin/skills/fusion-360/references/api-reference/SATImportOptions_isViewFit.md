# SATImportOptions.isViewFit Property

Parent Object: [SATImportOptions](SATImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/SATImportOptions.h>

## Description

Specifies if the camera should be adjusted to fit the geometry of the import. This defaults to true, which will cause a change in the current view. Setting this to false will leave the view as-is and just import the geometry.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sATImportOptions\_var" is a variable referencing a SATImportOptions object. |

"sATImportOptions\_var" is a variable referencing a SATImportOptions object. ```` ``` #include <Core/Application/SATImportOptions.h>  // Get the value of the property. boolean propertyValue = sATImportOptions_var->isViewFit();  // Set the value of the property, where value_var is a boolean. bool returnValue = sATImportOptions_var->isViewFit(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |