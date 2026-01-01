# PropertyGroup.itemById Method

Parent Object: [PropertyGroup](PropertyGroup.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/PropertyGroup.h>

## Description

Returns the specified property from the group using the unique ID of the property. The ID is consistent and can't be modified by the user and isn't affected by localization.

## Syntax

* [Python](#Python)
* [C++](#C++)

"propertyGroup\_var" is a variable referencing a [PropertyGroup](PropertyGroup.htm) object.```` ``` returnValue = propertyGroup_var.itemById(id) ``` ```` |

"propertyGroup\_var" is a variable referencing a [PropertyGroup](PropertyGroup.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Property](Property.htm) | Returns the specified Property or null if the ID doesn't match a property within the collection. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The unique ID of the property. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |