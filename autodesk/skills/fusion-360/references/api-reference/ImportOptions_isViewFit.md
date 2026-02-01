# ImportOptions.isViewFit Property

Parent Object: [ImportOptions](ImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ImportOptions.h>

## Description

Specifies if the camera should be adjusted to fit the geometry of the import. This defaults to true, which will cause a change in the current view. Setting this to false will leave the view as-is and just import the geometry.

## Syntax

* [Python](#Python)
* [C++](#C++)

"importOptions\_var" is a variable referencing an ImportOptions object. |

"importOptions\_var" is a variable referencing an ImportOptions object. ```` ``` #include <Core/Application/ImportOptions.h>  // Get the value of the property. boolean propertyValue = importOptions_var->isViewFit();  // Set the value of the property, where value_var is a boolean. bool returnValue = importOptions_var->isViewFit(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Import Manager API Sample](ImportManager_Sample.htm) | Demonstrates how to import different formats to Fusion document |

## Version

Introduced in version May 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |