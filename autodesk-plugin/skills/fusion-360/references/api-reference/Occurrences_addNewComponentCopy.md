# Occurrences.addNewComponentCopy Method

Parent Object: [Occurrences](Occurrences.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrences.h>

## Description

Method that creates a new occurrence by creating a new component that is a copy of an existing component. This is the equivalent of copying and using the "Paste New" command in the user interface. This is different from the addExistingComponent in that it's not a new instance to the existing component but a new component is created that has it's own definition (sketches, features, etc.) and a new occurrence instance is created to reference this new component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrences\_var" is a variable referencing an [Occurrences](Occurrences.htm) object.```` ``` returnValue = occurrences_var.addNewComponentCopy(component, transform) ``` ```` |

"occurrences\_var" is a variable referencing an [Occurrences](Occurrences.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Occurrence](Occurrence.htm) | Returns the newly created occurrence or null if the creation failed. The newly created component can be obtained by using the component property of the returned Occurrence. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| component | [Component](Component.htm) | The existing component to create a copy of. |
| transform | [Matrix3D](Matrix3D.htm) | A transform that defines the location for the new occurrence |

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |