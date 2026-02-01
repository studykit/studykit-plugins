# RevoluteJointMotion.objectType Property

Parent Object: [RevoluteJointMotion](RevoluteJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RevoluteJointMotion.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revoluteJointMotion\_var" is a variable referencing a RevoluteJointMotion object.  ```` ``` # Get the value of the property. propertyValue = revoluteJointMotion_var.objectType ``` ```` |

"revoluteJointMotion\_var" is a variable referencing a RevoluteJointMotion object. ```` ``` #include <Fusion/Components/RevoluteJointMotion.h>  // Get the value of the property. string propertyValue = revoluteJointMotion_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |