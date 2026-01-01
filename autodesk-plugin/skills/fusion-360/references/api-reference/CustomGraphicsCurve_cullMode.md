# CustomGraphicsCurve.cullMode Property

Parent Object: [CustomGraphicsCurve](CustomGraphicsCurve.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsCurve.h>

## Description

Gets and sets the culling model to use when rendering the entity. Culling is used when the entity contains a mesh or B-Rep faces and defines which sides of the mesh or face are rendered. This is primarily used for a watertight mesh or solid B-Rep so that the "inside" of the faces is not rendered since it's never visible to the user.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsCurve\_var" is a variable referencing a CustomGraphicsCurve object.  ```` ``` # Get the value of the property. propertyValue = customGraphicsCurve_var.cullMode  # Set the value of the property. customGraphicsCurve_var.cullMode = propertyValue ``` ```` |

"customGraphicsCurve\_var" is a variable referencing a CustomGraphicsCurve object. ```` ``` #include <Fusion/Graphics/CustomGraphicsCurve.h>  // Get the value of the property. CustomGraphicsCullModes propertyValue = customGraphicsCurve_var->cullMode();  // Set the value of the property, where value_var is a CustomGraphicsCullModes. bool returnValue = customGraphicsCurve_var->cullMode(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [CustomGraphicsCullModes](CustomGraphicsCullModes.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |