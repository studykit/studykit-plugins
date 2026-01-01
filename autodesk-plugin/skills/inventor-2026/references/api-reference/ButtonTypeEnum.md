# ButtonTypeEnum Enumerator

## Description

Button Types.

## Methods

|  |  |  |
| --- | --- | --- |
| Name | Value | Description |
| kAcceptButtonType | 2 | Implies that the user would like to continue despite the errors/warnings. The entire operation should return success, with the partially successful results committed to the document(s). |
| kCancelButtonType | 1 | Implies that the user does not want to continue. Any partial success during the execution is to be aborted. The command would have thus behaved like a no-op. |
| kEditButtonType | 4 | Implies that the user would like to go back into the command to correct the situation. The entire operation should be aborted, including any partial success and control should be returned back to the command. |

## Version

Introduced in version 2010
