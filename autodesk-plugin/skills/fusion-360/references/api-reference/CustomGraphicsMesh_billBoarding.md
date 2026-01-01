# CustomGraphicsMesh.billBoarding Property

Parent Object: [CustomGraphicsMesh](CustomGraphicsMesh.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsMesh.h>

## Description

Gets and sets the billboarding behavior of this custom graphics entity. To define billboarding you can set this property using a CustomGraphicsBillBoard objects that you statically create using the create method of the CustomGraphicsBillBoard class. To remove billboarding from this entity you can set this property to null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsMesh\_var" is a variable referencing a CustomGraphicsMesh object.  ```` ``` # Get the value of the property. propertyValue = customGraphicsMesh_var.billBoarding  # Set the value of the property. customGraphicsMesh_var.billBoarding = propertyValue ``` ```` |

"customGraphicsMesh\_var" is a variable referencing a CustomGraphicsMesh object. ```` ``` #include <Fusion/Graphics/CustomGraphicsMesh.h>  // Get the value of the property. Ptr<CustomGraphicsBillBoard> propertyValue = customGraphicsMesh_var->billBoarding();  // Set the value of the property, where value_var is a CustomGraphicsBillBoard. bool returnValue = customGraphicsMesh_var->billBoarding(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [CustomGraphicsBillBoard](CustomGraphicsBillBoard.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |