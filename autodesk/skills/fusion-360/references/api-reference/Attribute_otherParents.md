# Attribute.otherParents Property

Parent Object: [Attribute](Attribute.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Attribute.h>

## Description

In the case where the entity the attribute was originally placed on has been split, this property will return the other entities the attribute is associated with. For example, if an attribute is placed on a face and then a slot is created that cuts the face into two pieces and the attribute is available from both faces. The parent property returns the "primary" entity and this property returns any other entities, if any. If there aren't any other associated entities the ObjectCollection returned will be empty.

## Syntax

* [Python](#Python)
* [C++](#C++)

"attribute\_var" is a variable referencing an Attribute object. |

"attribute\_var" is a variable referencing an Attribute object. ```` ``` #include <Core/Application/Attribute.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = attribute_var->otherParents(); ``` ```` |

## Property Value

This is a read only property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |