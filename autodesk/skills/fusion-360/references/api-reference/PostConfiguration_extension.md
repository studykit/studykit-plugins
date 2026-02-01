# PostConfiguration.extension Property

Parent Object: [PostConfiguration](PostConfiguration.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Post/PostConfiguration.h>

## Description

Gets the extension of the output file created by the post.

## Syntax

* [Python](#Python)
* [C++](#C++)

"postConfiguration\_var" is a variable referencing a PostConfiguration object. |

"postConfiguration\_var" is a variable referencing a PostConfiguration object. ```` ``` #include <Cam/Post/PostConfiguration.h>  // Get the value of the property. string propertyValue = postConfiguration_var->extension(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Turning Workflow API Sample](Turning_Workflow_API_Sample_Sample.htm) | Turning Workflow API Sample This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |