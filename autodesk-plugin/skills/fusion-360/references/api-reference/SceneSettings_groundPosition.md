# SceneSettings.groundPosition Property

Parent Object: [SceneSettings](SceneSettings.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/SceneSettings.h>

## Description

Gets and sets the origin of the projection of the environment onto the textured ground plane. This lets you position the environment relative to the model. This is only used when the isGroundFlattened property is true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sceneSettings\_var" is a variable referencing a SceneSettings object.  ```` ``` # Get the value of the property. propertyValue = sceneSettings_var.groundPosition  # Set the value of the property. sceneSettings_var.groundPosition = propertyValue ``` ```` |

"sceneSettings\_var" is a variable referencing a SceneSettings object. ```` ``` #include <Fusion/Render/SceneSettings.h>  // Get the value of the property. Ptr<Point3D> propertyValue = sceneSettings_var->groundPosition();  // Set the value of the property, where value_var is a Point3D. bool returnValue = sceneSettings_var->groundPosition(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |