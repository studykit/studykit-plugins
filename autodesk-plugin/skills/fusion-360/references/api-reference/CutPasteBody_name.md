# CutPasteBody.name Property

Parent Object: [CutPasteBody](CutPasteBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CutPasteBody.h>

## Description

Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric).

## Syntax

* [Python](#Python)
* [C++](#C++)

"cutPasteBody\_var" is a variable referencing a CutPasteBody object. |

"cutPasteBody\_var" is a variable referencing a CutPasteBody object. ```` ``` #include <Fusion/Features/CutPasteBody.h>  // Get the value of the property. string propertyValue = cutPasteBody_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = cutPasteBody_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Cut Paste Bodies API Sample](CutPasteBodiesSample_Sample.htm) | Demonstrates how to use Cut Paste Bodies related API. |

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |