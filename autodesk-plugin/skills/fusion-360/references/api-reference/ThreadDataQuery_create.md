# ThreadDataQuery.create Method

Parent Object: [ThreadDataQuery](ThreadDataQuery.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadDataQuery.h>

## Description

Static method to create a new ThreadDataQuery object. The ThreadDataQuery object is a utility object that provides methods to query for the valid thread definitions defined in Fusion. This object provides similar functionality as the Thread and Hole command dialogs to find valid thread types, designations and classes which can be used to create thread and tapped hole features.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. ```` ```  #include <Fusion/Features/ThreadDataQuery.h> ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ThreadDataQuery](ThreadDataQuery.htm) | Returns a ThreadDataQuery object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| isTapered | boolean | Specifies if you want to query for standard or tapered holes.   This is an optional argument whose default value is False. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |