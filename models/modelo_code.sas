*****************************************;
** SAS Scoring Code for PROC Logistic;
*****************************************;

length I_compra $ 12;
label I_compra = 'Into: compra' ;
label U_compra = 'Unnormalized Into: compra' ;

label P_compra1 = 'Predicted: compra=1' ;
label P_compra0 = 'Predicted: compra=0' ;

drop _LMR_BAD;
_LMR_BAD=0;

*** Check interval variables for missing values;
if nmiss(edad,ingreso) then do;
   _LMR_BAD=1;
   goto _SKIP_000;
end;

*** Compute Linear Predictors;
drop _LP0;
_LP0 = 0;

*** Effect: edad;
_LP0 = _LP0 + (6.29193975521188) * edad;
*** Effect: ingreso;
_LP0 = _LP0 + (-0.00310633409253) * ingreso;

*** Predicted values;
drop _MAXP _IY _P0 _P1;
_TEMP = -25.5943599038615  + _LP0;
if (_TEMP < 0) then do;
   _TEMP = exp(_TEMP);
   _P0 = _TEMP / (1 + _TEMP);
end;
else _P0 = 1 / (1 + exp(-_TEMP));
_P1 = 1.0 - _P0;
P_compra1 = _P0;
_MAXP = _P0;
_IY = 1;
P_compra0 = _P1;
if (_P1 >  _MAXP + 1E-8) then do;
   _MAXP = _P1;
   _IY = 2;
end;
select( _IY );
   when (1) do;
      I_compra = '1' ;
      U_compra = 1;
   end;
   when (2) do;
      I_compra = '0' ;
      U_compra = 0;
   end;
   otherwise do;
      I_compra = '';
      U_compra = .;
   end;
end;
_SKIP_000:
if _LMR_BAD = 1 then do;
I_compra = '';
U_compra = .;
P_compra1 = .;
P_compra0 = .;
end;
drop _TEMP;
