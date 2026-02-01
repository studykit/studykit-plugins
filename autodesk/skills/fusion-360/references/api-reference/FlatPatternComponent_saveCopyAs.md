# FlatPatternComponent.saveCopyAs Method

Parent Object: [FlatPatternComponent](FlatPatternComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternComponent.h>

## Description

Performs a Save Copy As on this component. This saves the specified component as a new document in the specified location.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternComponent\_var" is a variable referencing a [FlatPatternComponent](FlatPatternComponent.htm) object.```` ``` returnValue = flatPatternComponent_var.saveCopyAs(name, dataFolder, description, tag) ``` ```` |

"flatPatternComponent\_var" is a variable referencing a [FlatPatternComponent](FlatPatternComponent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DataFileFuture](DataFileFuture.htm) | Returns a DataFileFuture object that can be used to track the progress of the upload and get the resulting DataFile once it's available on A360. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name to use for the new document. If this is an empty string, Fusion will use the name of the component being saved. |
| dataFolder | [DataFolder](DataFolder.htm) | The data folder to save the new document to. |
| description | string | The description string of the document. This can be an empty string. |
| tag | string | The tag string of the document. This can be an empty string. |

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |