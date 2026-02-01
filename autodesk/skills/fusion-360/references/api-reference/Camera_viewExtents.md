# Camera.viewExtents Property

Parent Object: [Camera](Camera.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Camera.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This property has been replaced by the getExtents and setExtents methods.

## Syntax

* [Python](#Python)
* [C++](#C++)

"camera\_var" is a variable referencing a Camera object.  ```` ``` # Get the value of the property. propertyValue = camera_var.viewExtents  # Set the value of the property. camera_var.viewExtents = propertyValue ``` ```` |

"camera\_var" is a variable referencing a Camera object. ```` ``` #include <Core/Application/Camera.h>  // Get the value of the property. double propertyValue = camera_var->viewExtents();  // Set the value of the property, where value_var is a double. bool returnValue = camera_var->viewExtents(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version August 2014
Retired in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |