% rebase('base.tpl', title="Vislice")

Geslo: {{geslo}} <br/>
Nepravilni ugibi: {{nepravilni}} <br/>
Stopnja obešenosti: {{obesenost}}
  <!-- <img src="img/10.jpg" alt="obesanje"> -->
% if stanje != model.ZMAGA and stanje != model.PORAZ:
<form action="" method="post">
    <input name="crka"> <input type="submit" value="Ugibaj">
</form>
% end