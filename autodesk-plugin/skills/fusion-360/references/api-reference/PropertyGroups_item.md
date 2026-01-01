# PropertyGroups.item Method

Parent Object: [PropertyGroups](PropertyGroups.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/PropertyGroups.h>

## Description

Returns the specified property group from the collection using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"propertyGroups\_var" is a variable referencing a [PropertyGroups](PropertyGroups.htm) object.```` ``` returnValue = propertyGroups_var.item(index) ``` ```` |

"propertyGroups\_var" is a variable referencing a [PropertyGroups](PropertyGroups.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PropertyGroup](PropertyGroup.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | integer | The index of the property within the collection where the first item is 0. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |