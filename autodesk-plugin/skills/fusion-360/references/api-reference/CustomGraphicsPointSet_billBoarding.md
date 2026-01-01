# CustomGraphicsPointSet.billBoarding Property

Parent Object: [CustomGraphicsPointSet](CustomGraphicsPointSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsPointSet.h>

## Description

Gets and sets the billboarding behavior of this custom graphics entity. To define billboarding you can set this property using a CustomGraphicsBillBoard objects that you statically create using the create method of the CustomGraphicsBillBoard class. To remove billboarding from this entity you can set this property to null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsPointSet\_var" is a variable referencing a CustomGraphicsPointSet object.  ```` ``` # Get the value of the property. propertyValue = customGraphicsPointSet_var.billBoarding  # Set the value of the property. customGraphicsPointSet_var.billBoarding = propertyValue ``` ```` |

"customGraphicsPointSet\_var" is a variable referencing a CustomGraphicsPointSet object. ```` ``` #include <Fusion/Graphics/CustomGraphicsPointSet.h>  // Get the value of the property. Ptr<CustomGraphicsBillBoard> propertyValue = customGraphicsPointSet_var->billBoarding();  // Set the value of the property, where value_var is a CustomGraphicsBillBoard. bool returnValue = customGraphicsPointSet_var->billBoarding(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [CustomGraphicsBillBoard](CustomGraphicsBillBoard.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |