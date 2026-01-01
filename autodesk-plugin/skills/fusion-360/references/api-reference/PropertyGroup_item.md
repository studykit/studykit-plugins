# PropertyGroup.item Method

Parent Object: [PropertyGroup](PropertyGroup.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/PropertyGroup.h>

## Description

Returns the specified property from the group using an index into the group.

## Syntax

* [Python](#Python)
* [C++](#C++)

"propertyGroup\_var" is a variable referencing a [PropertyGroup](PropertyGroup.htm) object.```` ``` returnValue = propertyGroup_var.item(index) ``` ```` |

"propertyGroup\_var" is a variable referencing a [PropertyGroup](PropertyGroup.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Property](Property.htm) | Returns the specified group or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | integer | The index of the property within the group where the first item is 0. |

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