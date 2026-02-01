# Occurrences.addByInsert Method

Parent Object: [Occurrences](Occurrences.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrences.h>

## Description

Method that inserts an existing file.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrences\_var" is a variable referencing an [Occurrences](Occurrences.htm) object.```` ``` returnValue = occurrences_var.addByInsert(dataFile, transform, isReferencedComponent) ``` ```` |

"occurrences\_var" is a variable referencing an [Occurrences](Occurrences.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Occurrence](Occurrence.htm) | Returns the newly created occurrence or null if the insert failed. Insert will fail if the dataFile being inserted is not from the same project as the document it is being inserted into while isReferencedComponent is True. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| dataFile | [DataFile](DataFile.htm) | The dataFile to insert. |
| transform | [Matrix3D](Matrix3D.htm) | A transform that defines the location for the new occurrence. |
| isReferencedComponent | boolean | Indicates if the insert is to be an external reference or embedded within this document. This method will fail if the dataFile being inserted is not from the same project as the document it is being inserted into while isReferencedComponent is True. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Save and Insert File API Sample](SaveAndInsertSample_Sample.htm) | Demonstrates creating save a new file and then inserting it into a design. To use this sample, have a design open that has been saved and run the script. It will create a new design that contains a cylinder, save it to the same folder the active design was saved to, and then insert it into the active design. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |