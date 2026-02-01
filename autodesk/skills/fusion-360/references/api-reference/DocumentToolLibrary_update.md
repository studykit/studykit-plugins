# DocumentToolLibrary.update Method

Parent Object: [DocumentToolLibrary](DocumentToolLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/DocumentToolLibrary.h>

## Description

Update the given tool in the document tool library. The update applies all changes to the tool in the document tool library and therefore on all operations that use the tool. Will error if the tool does not exist in the document tool library.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentToolLibrary\_var" is a variable referencing a [DocumentToolLibrary](DocumentToolLibrary.htm) object.```` ``` returnValue = documentToolLibrary_var.update(tool, updateFeedAndSpeed) ``` ```` |

"documentToolLibrary\_var" is a variable referencing a [DocumentToolLibrary](DocumentToolLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the update was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| tool | [Tool](Tool.htm) | The tool that should be updated. |
| updateFeedAndSpeed | boolean | Setting updateFeedAndSpeed to true will override the feed and speed parameters of operations within the document which use the given tool. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |