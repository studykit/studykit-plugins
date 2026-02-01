# PropertyGroups.itemById Method

Parent Object: [PropertyGroups](PropertyGroups.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/PropertyGroups.h>

## Description

Returns the specified property group from the collection using the unique ID of the property group. The ID is consistent and can't be modified by the user and isn't affected by localization.

## Syntax

* [Python](#Python)
* [C++](#C++)

"propertyGroups\_var" is a variable referencing a [PropertyGroups](PropertyGroups.htm) object.```` ``` returnValue = propertyGroups_var.itemById(id) ``` ```` |

"propertyGroups\_var" is a variable referencing a [PropertyGroups](PropertyGroups.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PropertyGroup](PropertyGroup.htm) | Returns the specified PropertyGroup or null if the ID doesn't match a group within the collection. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The unique ID of the property group. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Library Item API Sample](LibraryItemSample_Sample.htm) | Demonstrates how to examine library items using the API.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the existing default code. The script will search for and record all components and library items in the current project. They are displayed in a dialog when the script has finished. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |