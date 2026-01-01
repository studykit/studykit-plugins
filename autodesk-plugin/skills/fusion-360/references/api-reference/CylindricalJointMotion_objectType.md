# CylindricalJointMotion.objectType Property

Parent Object: [CylindricalJointMotion](CylindricalJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/CylindricalJointMotion.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cylindricalJointMotion\_var" is a variable referencing a CylindricalJointMotion object.  ```` ``` # Get the value of the property. propertyValue = cylindricalJointMotion_var.objectType ``` ```` |

"cylindricalJointMotion\_var" is a variable referencing a CylindricalJointMotion object. ```` ``` #include <Fusion/Components/CylindricalJointMotion.h>  // Get the value of the property. string propertyValue = cylindricalJointMotion_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |