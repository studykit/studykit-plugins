# ProductPreferencesCollection.item Method

Parent Object: [ProductPreferencesCollection](ProductPreferencesCollection.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ProductPreferencesCollection.h>

## Description

Function that returns the specified ProductPreferences object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"productPreferencesCollection\_var" is a variable referencing a [ProductPreferencesCollection](ProductPreferencesCollection.htm) object.```` ``` returnValue = productPreferencesCollection_var.item(index) ``` ```` |

"productPreferencesCollection\_var" is a variable referencing a [ProductPreferencesCollection](ProductPreferencesCollection.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ProductPreferences](ProductPreferences.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |