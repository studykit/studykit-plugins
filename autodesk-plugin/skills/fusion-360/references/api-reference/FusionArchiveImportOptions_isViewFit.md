# FusionArchiveImportOptions.isViewFit Property

Parent Object: [FusionArchiveImportOptions](FusionArchiveImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/FusionArchiveImportOptions.h>

## Description

Specifies if the camera should be adjusted to fit the geometry of the import. This defaults to true, which will cause a change in the current view. Setting this to false will leave the view as-is and just import the geometry.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionArchiveImportOptions\_var" is a variable referencing a FusionArchiveImportOptions object. |

"fusionArchiveImportOptions\_var" is a variable referencing a FusionArchiveImportOptions object. ```` ``` #include <Core/Application/FusionArchiveImportOptions.h>  // Get the value of the property. boolean propertyValue = fusionArchiveImportOptions_var->isViewFit();  // Set the value of the property, where value_var is a boolean. bool returnValue = fusionArchiveImportOptions_var->isViewFit(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |