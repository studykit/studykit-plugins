# PropertyGroups.itemByName Method

Parent Object: [PropertyGroups](PropertyGroups.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/PropertyGroups.h>

## Description

Returns the specified PropertyGroup using the name of the group.

## Syntax

* [Python](#Python)
* [C++](#C++)

"propertyGroups\_var" is a variable referencing a [PropertyGroups](PropertyGroups.htm) object.```` ``` returnValue = propertyGroups_var.itemByName(name) ``` ```` |

"propertyGroups\_var" is a variable referencing a [PropertyGroups](PropertyGroups.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PropertyGroup](PropertyGroup.htm) | Returns the specified group or null if the name doesn't match a group within the collection. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the group to return. This is the name as seen in the user interface. Not all groups have a name. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |