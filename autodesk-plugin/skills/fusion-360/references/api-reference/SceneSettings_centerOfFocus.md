# SceneSettings.centerOfFocus Property

Parent Object: [SceneSettings](SceneSettings.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/SceneSettings.h>

## Description

When the isDepthofFieldEnabled property is true, this point is used as the center of focus. All objects that are the same distance from the camera as this point will be in focus. Any geometry that is closer or further away from the camera than this point will appear more out of focus.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sceneSettings\_var" is a variable referencing a SceneSettings object.  ```` ``` # Get the value of the property. propertyValue = sceneSettings_var.centerOfFocus  # Set the value of the property. sceneSettings_var.centerOfFocus = propertyValue ``` ```` |

"sceneSettings\_var" is a variable referencing a SceneSettings object. ```` ``` #include <Fusion/Render/SceneSettings.h>  // Get the value of the property. Ptr<Point3D> propertyValue = sceneSettings_var->centerOfFocus();  // Set the value of the property, where value_var is a Point3D. bool returnValue = sceneSettings_var->centerOfFocus(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |