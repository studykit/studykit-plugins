# ApplicationEvents.OnCloseDocument Event

Parent Object: [ApplicationEvents](../ApplicationEvents/ApplicationEvents.md)

## Description

Event that is fired whenever a document is closed.

## Remarks

Note : The OnOpenDocument and OnCloseDocument events fire when the document is initially opened and finally closed. This means if the file is referenced from an assembly, OnOpenDocument will not fire if a loaded file referenced in an open assembly is opened again, as internally this file is already open. Conversely, if a document is closed, the document is not really closed unless that was the final view and the document is not referenced by any other open documents. To Veto the OnCloseDocument event. When a document is about to be closed, the OnCloseDocument Application event is fired with the BeforeOrAfter argument set to kBefore. If the event handler returns HandlingCode argument set to kEventCancelled, the close operation is cancelled. Inventor then fires a corresponding kAbort event. For example:

## Syntax

ApplicationEvents.**OnCloseDocument**( ***DocumentObject*** As [Document](../Document/Document.md), ***FullDocumentName*** As String, ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | The Document object that is being closed. The document being closed is provided for both the kBefore and kAfter cases. This is because the Document is still available after it's closed, although in a limited sense, until it is terminated. One of the useful things you can do with a document in this state is to compare it's identity with a reference previously saved (usually during kBefore). For example: Private m\_oClosingDoc As Object  Private Sub AppEvents\_OnCloseDocument(ByVal DocumentObject As Document, ByVal FullDocumentName As String, ByVal BeforeOrAfter As EventTimingEnum, ByVal Context As NameValueMap, HandlingCode As HandlingCodeEnum)     If BeforeOrAfter = kBefore Then         ' Check to see if the Document being closed is an interesting one.         If Interesting(DocumentObject) Then             ' Save a reference to the object.             Set m\_oClosingDoc = DocumentObject         End If     Else         ' Now we're either after the close or it's been aborted. Check to see if the document is the interesting one.         If DocumentObject Is m\_oClosingDoc Then             If BeforeOrAfter = kAfter Then             ' The document was closed.             ElseIf BeforeOrAfter = kAbort Then             ' The close was aborted.             End If         End If     End If  End Sub |
| FullDocumentName | String | Output string that specifies the fully qualified name of the document being closed. This is supplied both before and after. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input indicating if the event is being fired before (kBefore) or after (kAfter) the document is closed. Notification is sent before and after the document is closed. In the case where this event is canceled the value of this argument will be kAbort. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input object that can be used to determine the context of why the event fired. This event provides additional information through the Context argument as described below: Name = "HealthStatusEnum", Value = The health status of the document. If this value is anything other than kUpToDateHealth you know the Document object returned is not in a state where you can use most of its methods or properties. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | This event supports the ability to cancel the close. By setting this argument to kEventCanceled when the BeforeOrAfter argument is kBefore Inventor will abort the close. When the close is cancelled, this event is fired again but the BeforeOrAfter argument will have a value of kAbort. |

## Version

Introduced in version 4
