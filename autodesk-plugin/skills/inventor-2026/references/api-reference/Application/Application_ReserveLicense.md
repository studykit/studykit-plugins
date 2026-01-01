# Application.ReserveLicense Method

Parent Object: [Application](../Application/Application.md)

## Description

Informs Inventor/Apprentice that a license should be retained for this instance of the application. Used to prevent idle detection from returning the seat license to the license pool. Requires a call to UnreserveLicense with the same ClientID to allow license reclamation to resume.

## Syntax

Application.**ReserveLicense**( ***ClientId*** As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ClientId | String |  |

## Version

Introduced in version 2009
