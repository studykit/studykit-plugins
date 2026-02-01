# Property.parent Property

Parent Object: [Property](Property.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Property.h>

## Description

Returns the parent of this property.For properties associated with an appearance this will return the parent Appearance. For properties associated with a material, this will return the parent Material. For other types of properties, this will return the PropertyGroup it is in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"property\_var" is a variable referencing a Property object. |

"property\_var" is a variable referencing a Property object. ```` ``` #include <Core/Application/Property.h>  // Get the value of the property. Ptr<Base> propertyValue = property_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |