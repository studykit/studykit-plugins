# CustomGraphicsGroup.billBoarding Property

Parent Object: [CustomGraphicsGroup](CustomGraphicsGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsGroup.h>

## Description

Gets and sets the billboarding behavior of this custom graphics entity. To define billboarding you can set this property using a CustomGraphicsBillBoard objects that you statically create using the create method of the CustomGraphicsBillBoard class. To remove billboarding from this entity you can set this property to null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsGroup\_var" is a variable referencing a CustomGraphicsGroup object.  ```` ``` # Get the value of the property. propertyValue = customGraphicsGroup_var.billBoarding  # Set the value of the property. customGraphicsGroup_var.billBoarding = propertyValue ``` ```` |

"customGraphicsGroup\_var" is a variable referencing a CustomGraphicsGroup object. ```` ``` #include <Fusion/Graphics/CustomGraphicsGroup.h>  // Get the value of the property. Ptr<CustomGraphicsBillBoard> propertyValue = customGraphicsGroup_var->billBoarding();  // Set the value of the property, where value_var is a CustomGraphicsBillBoard. bool returnValue = customGraphicsGroup_var->billBoarding(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [CustomGraphicsBillBoard](CustomGraphicsBillBoard.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |