# BRepBody.isLightBulbOn Property

Parent Object: [BRepBody](BRepBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBody.h>

## Description

Gets and set if the light bulb beside the body node in the browser is on or not. Parent nodes in the browser can have their light bulb off which affects all of their children so this property does not indicate if the body is actually visible, just that it should be visible if all of it's parent nodes are also visible. Use the isVisible property to determine if it's actually visible.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBody\_var" is a variable referencing a BRepBody object.  ```` ``` # Get the value of the property. propertyValue = bRepBody_var.isLightBulbOn  # Set the value of the property. bRepBody_var.isLightBulbOn = propertyValue ``` ```` |

"bRepBody\_var" is a variable referencing a BRepBody object. ```` ``` #include <Fusion/BRep/BRepBody.h>  // Get the value of the property. boolean propertyValue = bRepBody_var->isLightBulbOn();  // Set the value of the property, where value_var is a boolean. bool returnValue = bRepBody_var->isLightBulbOn(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BRep Body Sample](BRepBodySample_Sample.htm) | B-Rep (Boundary Representation) body related functions |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |