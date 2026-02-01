# Attributes.groupNames Property

Parent Object: [Attributes](Attributes.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Attributes.h>

## Description

Returns an array of strings that are all of the name of attribute groups that exist on this entity. An empty array can be returns if there are no attributes on the entity.

## Syntax

* [Python](#Python)
* [C++](#C++)

"attributes\_var" is a variable referencing an Attributes object. |

"attributes\_var" is a variable referencing an Attributes object. ```` ``` #include <Core/Application/Attributes.h>  // Get the value of the property. std::vector<string> propertyValue = attributes_var->groupNames(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type string.

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |