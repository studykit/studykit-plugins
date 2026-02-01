# Appearance.usedBy Property

Parent Object: [Appearance](Appearance.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/Appearance.h>

## Description

Returns a collection of the entities currently using this appearance. This property is only valid for an appearance in a Design and where the IsUsed property returns true. The collection returned can contain

## Syntax

* [Python](#Python)
* [C++](#C++)

"appearance\_var" is a variable referencing an Appearance object. |

"appearance\_var" is a variable referencing an Appearance object. ```` ``` #include <Core/Materials/Appearance.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = appearance_var->usedBy(); ``` ```` |

## Property Value

This is a read only property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |