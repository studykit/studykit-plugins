# ApplicationEvents.OnMigrateDocument Event

Parent Object: [ApplicationEvents](../ApplicationEvents/ApplicationEvents.md)

## Description

Event that is fired whenever a document is being explicitly migrated.

## Remarks

Explicit migration can occur in one of the following situations: \* User selects the Migrate command thru the user interface. \* The Document.Migrate method is called via the API on a document needing migration. \* A document needing migration is saved. The event fires after Inventor has completed migration of core data. This event provides an opportunity for client AddIns to migrate their data. The OnMigrateDocument event notifies a client when a document is being fully migrated. Migration is the process of updating the data within a document created in an older version of Inventor to the data format of the current version. With delayed migration, documents created in Inventor version 11 and newer are not fully migrated until a modified document is saved or the end-user executes the Migrate command. This event is intended to be used by applications that are storing application specific data within the Inventor document and may also need to migrate their data from one version to another. They can use this event as one trigger to migrate. Other triggers, besides this event, may be when the end-user attempts to modify their data or runs one of their commands that needs up to date data to operate on.

## Syntax

ApplicationEvents.**OnMigrateDocument**( ***DocumentObject*** As [Document](../Document/Document.md), ***BeforeOrAfter*** As [EventTimingEnum](../EventTimingEnum.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DocumentObject | [Document](../Document/Document.md) | Input Document object that is being migrated. |
| BeforeOrAfter | [EventTimingEnum](../EventTimingEnum.md) | Input EventTimingEnum indicating if the event is being fired before (kBefore) or after (kAfter) the document is migrated. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap object that can be used to determine the context of why the event fired. No context information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output HandlingCodeEnum that indicates how you are handling the event. This argument is ignored for this event. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |