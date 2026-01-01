# EventArgs Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/EventArgs.h>

## Description

When an event handler is called, it is passed an EventArgs object that describes the 'event'. This is a base class - classes like DocumentEventArgs add more information on the 'event'.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](EventArgs_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [firingEvent](EventArgs_firingEvent.htm) | The event that the firing is in response to. |
| [isValid](EventArgs_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](EventArgs_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Derived Classes

[ActiveSelectionEventArgs](ActiveSelectionEventArgs.htm), [ApplicationCommandEventArgs](ApplicationCommandEventArgs.htm), [ApplicationEventArgs](ApplicationEventArgs.htm), [CameraEventArgs](CameraEventArgs.htm), [CommandCreatedEventArgs](CommandCreatedEventArgs.htm), [CommandEventArgs](CommandEventArgs.htm), [CustomEventArgs](CustomEventArgs.htm), [CustomFeatureEventArgs](CustomFeatureEventArgs.htm), [DataEventArgs](DataEventArgs.htm), [DocumentEventArgs](DocumentEventArgs.htm), [HTMLEventArgs](HTMLEventArgs.htm), [HttpEventArgs](HttpEventArgs.htm), [InputChangedEventArgs](InputChangedEventArgs.htm), [KeyboardEventArgs](KeyboardEventArgs.htm), [MarkingMenuEventArgs](MarkingMenuEventArgs.htm), [MFGDMDataEventArgs](MFGDMDataEventArgs.htm), [MouseEventArgs](MouseEventArgs.htm), [NavigationEventArgs](NavigationEventArgs.htm), [RenderEventArgs](RenderEventArgs.htm), [SelectionEventArgs](SelectionEventArgs.htm), [SetupChangeEventArgs](SetupChangeEventArgs.htm), [SetupEventArgs](SetupEventArgs.htm), [UserInterfaceGeneralEventArgs](UserInterfaceGeneralEventArgs.htm), [ValidateInputsEventArgs](ValidateInputsEventArgs.htm), [WebRequestEventArgs](WebRequestEventArgs.htm), [WorkspaceEventArgs](WorkspaceEventArgs.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |