# WebRequestEventArgs Object

Derived from: [EventArgs](EventArgs.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/WebRequestEventArgs.h>

## Description

The WebRequestEventArgs provides information associated with a web request event. These are events fired as a result of a Fusion protocol handler being invoked from a web page. Note that some properties are not available on every event.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](WebRequestEventArgs_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [file](WebRequestEventArgs_file.htm) | Returns the value specified as the "file" parameter in the URL. |
| [firingEvent](WebRequestEventArgs_firingEvent.htm) | The event that the firing is in response to. |
| [id](WebRequestEventArgs_id.htm) | Returns the value specified as the "id" parameter in the URL. This will be decoded. It can be an empty string if the "id" parameter was not specified in the URL. |
| [isCanceled](WebRequestEventArgs_isCanceled.htm) | Used during the insertingFromURL and openingFromURL events to get or set if the insert or open should be allowed to continue. This defaults to false, which will allow the operation to continue as normal. This property should be ignored for all events besides the insertingFromURL and openingFromURL events. |
| [isValid](WebRequestEventArgs_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](WebRequestEventArgs_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [occurrenceOrDocument](WebRequestEventArgs_occurrenceOrDocument.htm) | Used during the insertedFromURL or openedFromURL events and returns the Document (openedFromURL) or Occurrence (insertedFromURL) that was just created. |
| [privateInfo](WebRequestEventArgs_privateInfo.htm) | Returns the value specified as the "privateInfo" parameter in the URL. This will be decoded and can be an empty string if the "privateInfo" parameter was not specified in the URL. |
| [properties](WebRequestEventArgs_properties.htm) | Returns the value specified as the "properties" parameter in the URL. This will be decoded and should be in JSON format if it was properly provided by the web page. It can be an empty string if the "properties" parameter was not specified in the URL. |

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |