# NamedViews.itemByName Method

Parent Object: [NamedViews](NamedViews.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/NamedViews.h>

## Description

Returns the specified named view using the name of the named view. The four standard named views ("TOP", "FRONT", "RIGHT", and "HOME") are not accessible through this method. For the predefined view use the properties on this collection that provide direct access to the specific named view.

## Syntax

* [Python](#Python)
* [C++](#C++)

"namedViews\_var" is a variable referencing a [NamedViews](NamedViews.htm) object.```` ``` returnValue = namedViews_var.itemByName(name) ``` ```` |

"namedViews\_var" is a variable referencing a [NamedViews](NamedViews.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [NamedView](NamedView.htm) | Returns null if the specified name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the named view within the collection to return. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |