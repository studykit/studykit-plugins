# Attributes.itemsByGroup Method

Parent Object: [Attributes](Attributes.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Attributes.h>

## Description

Returns an array of all of the attributes that belong to the specified group.

## Syntax

* [Python](#Python)
* [C++](#C++)

"attributes\_var" is a variable referencing an [Attributes](Attributes.htm) object.```` ``` returnValue = attributes_var.itemsByGroup(groupName) ``` ```` |

"attributes\_var" is a variable referencing an [Attributes](Attributes.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Attribute](Attribute.htm)[] | Returns an array of attributes or will fail in the case where an invalid group name is specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| groupName | string | The name of the group. |

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |