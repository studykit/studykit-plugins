# ModelHoleThreadNoteDefinition Object

## Description

The ModelHoleThreadNoteDefinition provides access to all of the information that defines a hole or thread note.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_Copy.md) | Method that creates a copy of this ModelHoleThreadNoteDefinition object. The new ModelHoleThreadNoteDefinition object is independent of any note. It can be edited and used as input to edit an existing note or to create a new note. |
| [GetHolePropertyTolerance](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_GetHolePropertyTolerance.md) | Method that gets the tolerance for the specified hole property. |
| [GetHolePropertyTolerancePrecision](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_GetHolePropertyTolerancePrecision.md) | Method that gets the tolerance precision for the specified hole property. |
| [GetHolePropertyToleranceStatus](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_GetHolePropertyToleranceStatus.md) | Method that returns whether the tolerance for the specified hole property is enabled or not. This returns True if the hole property tolerance is enabled. |
| [IsValidAnnotationPlane](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_IsValidAnnotationPlane.md) | Method that returns the wheather a planer object is valid to be used as an annotation plane for this hole or thread note. |
| [SetHolePropertyTolerancePrecision](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_SetHolePropertyTolerancePrecision.md) | Method that sets the tolerance precision for the specified hole property. |
| [SetHolePropertyToleranceStatus](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_SetHolePropertyToleranceStatus.md) | Method that enables/disables the tolerance for the specified hole property. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnnotationPlane](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_AnnotationPlane.md) | Read-write property that gets and sets the annotation plane for the hole or thread note. Will return nothing in case where the ModelHoleThreadNodeDefinition object is transient and not associated with a hole or thread note. |
| [AnnotationPlaneDefinition](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_AnnotationPlaneDefinition.md) | Read-write property that gets and sets the annotation plane definition for the hole or thread note. |
| [Application](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [ArrowheadType](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_ArrowheadType.md) | Read-write property that gets and sets the type of the arrowhead. This is a style override. |
| [FormattedHoleThreadNote](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_FormattedHoleThreadNote.md) | Read-write property that gets and sets the fully formatted string that defines the contents of the hole or thread text. The formatting is specified using XML tags within the string. By default, all text in the string will be displayed using the defaults specified in the dimension style. You can use the XML tags to override the default style and apply style overrides for all or portions of the text. The formatting overrides are defined using tags. There is an opening tag and closing tag for each formatting override you define. The text between the opening and closing tags is affected by the override. |
| [Intent](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_Intent.md) | Read-write property that gets and sets the geometry associated with the hole or thread note. |
| [IsHoleNote](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_IsHoleNote.md) | Read-write property that indicates if this note is for a hole or thread feature. Returns True if it is for a hole note. This is true even in the case where the hole is tapped and has threads. Returns False in the case where the note is for a thread feature. Th. |
| [IsTapDrill](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_IsTapDrill.md) | Read-write property that gets and sets whether to set the hole note as tap drill type. This property only applies to tapped hole features. In other cases the value of this property should be ignored and setting it will fail. |
| [LandingPosition](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_LandingPosition.md) | Read-write property that gets and sets the landing position of the dimension. The point is projected onto the orientation plane. |
| [Parent](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_Parent.md) | Read-only property that returns the parent model annotation that the definition is associated with. This property will return Nothing in the case where the definition is not associated with any annotation. This is the case when it’s been created using one of the create definition methods and when it’s been copied from another definition object. |
| [RightHandedThread](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_RightHandedThread.md) | Gets and sets whether to show RH for right handed thread. |
| [Text](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_Text.md) | Read-only property that gets the text of the dimension. Properties on the returned ModelAnnotationText object can be edited to change the displayed text. |
| [TextPosition](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_TextPosition.md) | Read-write property that controls the position of the hole or thread note text. When being set, the input point will be projected onto the orientation plane. |
| [Type](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseCustomThreadDesignation](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_UseCustomThreadDesignation.md) | Gets and sets whether to use the custom thread designation, as defined in the Thread.xls spreadsheet for thread notes. |
| [UseDefaultFormat](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_UseDefaultFormat.md) | Gets and sets whether to use the default format for hole notes. |
| [UseModelUnits](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_UseModelUnits.md) | Read-write property that gets and sets whether to use the model measurement units for hole note. This is only valid for notes to hole features and not notes to thread features. This can easily be determined by checking the value of IsHoleNote property. In other cases the value of this property should be ignored and setting it will fail. |
| [UseParameterTolerance](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_UseParameterTolerance.md) | Read-write property that gets and sets whether to use the format and tolerance information from parameters for hole note. This is only valid for notes to hole features and not notes to thread features. This can easily be determined by checking the value of IsHoleNote property. In other cases the value of this property should be ignored and setting it will fail. |

## Accessed From

[ModelHoleThreadNote.Definition](../ModelHoleThreadNote/ModelHoleThreadNote_Definition.md), [ModelHoleThreadNoteDefinition.Copy](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_Copy.md), [ModelHoleThreadNoteProxy.Definition](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_Definition.md), [ModelHoleThreadNotes.CreateDefinition](../ModelHoleThreadNotes/ModelHoleThreadNotes_CreateDefinition.md)

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |