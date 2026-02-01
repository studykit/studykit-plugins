# CAMTemplate.createHoleTemplateFromOperations Method

Parent Object: [CAMTemplate](CAMTemplate.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAMTemplate/CAMTemplate.h>

## Description

Create a hole CAMTemplate from a list of hole operations. Hole templates may be used in Hole Recognition

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CAMTemplate](CAMTemplate.htm) | Returns the newly created template. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| operations | Operation[] | A list of operations to bundle into a template. Only 2D Adaptive, 2D Chamfer, 2D Contour, 2D Pocket, Bore, Circular, Drill and Thread operations are allowed in hole templates. Passing in other operation types will throw an error. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |