# NamedViews.item Method

Parent Object: [NamedViews](NamedViews.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/NamedViews.h>

## Description

Returns the specified named view using an index into the collection. The four standard named views ("TOP", "FRONT", "RIGHT", and "HOME") are not accessible through this method. For the predefined view use the properties on this collection that provide direct access to the specific named view.

## Syntax

* [Python](#Python)
* [C++](#C++)

"namedViews\_var" is a variable referencing a [NamedViews](NamedViews.htm) object.```` ``` returnValue = namedViews_var.item(index) ``` ```` |

"namedViews\_var" is a variable referencing a [NamedViews](NamedViews.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [NamedView](NamedView.htm) | Returns the specified named view or an error if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the named view within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |