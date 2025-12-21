# Application.UnreserveLicense Method

Parent Object: [Application](../Application/Application.md)

## Description

Informs Inventor/Apprentice that normal seat license reclamation can resume. Use this method when extended processing for which a license was reserved completes. Do not use without a previous call to ReserveLicense using the same ClientID.

## Syntax

Application.**UnreserveLicense**( ***ClientId*** As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ClientId | String |  |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |