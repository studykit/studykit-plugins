# CustomGraphicsPointSet.pointType Property

Parent Object: [CustomGraphicsPointSet](CustomGraphicsPointSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsPointSet.h>

## Description

Specifies which of the predefined point images to use. Attempting to set this property to UserDefinedCustomGraphicsPointType will fail. To change to a user defined point type you must set use the pointImage property to specify the image to use and this will have the side-effect of changing the value of this property to UserDefinedCustomGraphicsPointType.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsPointSet\_var" is a variable referencing a CustomGraphicsPointSet object. |

"customGraphicsPointSet\_var" is a variable referencing a CustomGraphicsPointSet object. ```` ``` #include <Fusion/Graphics/CustomGraphicsPointSet.h>  // Get the value of the property. CustomGraphicsPointTypes propertyValue = customGraphicsPointSet_var->pointType();  // Set the value of the property, where value_var is a CustomGraphicsPointTypes. bool returnValue = customGraphicsPointSet_var->pointType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [CustomGraphicsPointTypes](CustomGraphicsPointTypes.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |